use unrar::Archive as UnrarArchive;
use walkdir::WalkDir;
use zip::ZipArchive;
use rusqlite::{params, Connection, Result as SqliteResult};
use std::fs::File;
use std::io::{Cursor, Read};
use std::path::Path;
use serde::{Serialize, Deserialize};
pub async fn scan_directory_and_store_comic_info_async<P: AsRef<Path> + Send + 'static>(path: P, db_path: String) -> Result<(), rusqlite::Error> {
    tokio::task::spawn_blocking(move || scan_directory_and_store_comic_info(path, &db_path)).await.unwrap()
}

#[derive(Serialize, Deserialize)]
pub struct ComicInfo {
    id: i32,
    content: String,
}

fn scan_directory_and_store_comic_info<P: AsRef<Path>>(path: P, db_path: &str) -> SqliteResult<()> {
    let conn = Connection::open(db_path)?;

    conn.execute(
        "CREATE TABLE IF NOT EXISTS comic_info (id INTEGER PRIMARY KEY, content TEXT NOT NULL)",
        [],
    )?;

    for entry in WalkDir::new(path)
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| e.path().extension().map_or(false, |ext| ext == "cbz" || ext == "cbr"))
    {
        let path = entry.path();
        if path.extension().unwrap() == "cbz" {
            // Process .cbz files (ZIP archives)
            let file = File::open(path)?;
            let mut archive = ZipArchive::new(file)?;

            for i in 0..archive.len() {
                let mut file = archive.by_index(i)?;
                if file.name().ends_with("comicinfo.xml") {
                    let mut contents = String::new();
                    file.read_to_string(&mut contents)?;

                    conn.execute(
                        "INSERT INTO comic_info (content) VALUES (?1)",
                        params![contents],
                    )?;
                }
            }
        } else {
            // Process .cbr files (RAR archives)
            let archive_path = path.to_str().expect("Path to string conversion failed");
            for entry in UnrarArchive::new(archive_path.to_string()).open_for_listing().unwrap() {
                let entry = entry.unwrap();
                if entry.filename.ends_with("comicinfo.xml") {
                    let mut contents = Vec::new();
                    // Open the archive again for processing to extract the comicinfo.xml file
                    let mut archive_for_extraction = UnrarArchive::new(archive_path.to_string()).open_for_processing().unwrap();
                    while let Some(header) = archive_for_extraction.read_header().unwrap() {
                        if header.filename == entry.filename {
                            let (data, _) = header.read().unwrap();
                            contents = data;
                            break;
                        } else {
                            // Move to the next file in the archive
                            archive_for_extraction.skip().unwrap();
                        }
                    }
                    let contents_str = String::from_utf8(contents).expect("Failed to convert bytes to string");
                    conn.execute(
                        "INSERT INTO comic_info (content) VALUES (?1)",
                        params![contents_str],
                    )?;
                }
            }
        }
    }

    Ok(())
}
