use axum::{
    routing::{get, post},
    Router,
    Json,
};
use hyper::server;
use serde::{Serialize, Deserialize};
use rusqlite::{Connection, Result};
use std::net::SocketAddr;
mod routes;
mod modules {
    pub mod filehandler;
}
use modules::filehandler::{ComicInfo, scan_directory_and_store_comic_info_async}; // Adjust according to your actual module structure

#[derive(Serialize)]
struct ComicResponse {
    id: i32,
    content: String,
}


async fn list_comics_async(dbpath: String) -> Json<Vec<ComicInfo>> {
    let conn = Connection::open(dbpath).unwrap(); // In production, handle errors properly

    let mut stmt = conn.prepare("SELECT id, content FROM comic_info").unwrap();
    let comic_iter = stmt.query_map([], |row| {
        Ok(ComicInfo {
            id: row.get(0)?,
            content: row.get(1)?,
        })
    }).unwrap();

    let comics: Vec<ComicInfo> = comic_iter.into_iter().filter_map(Result::ok).collect();

    Json(comics)
}

async fn list_comics_handler(dbpath: String) -> Json<Vec<ComicResponse>> {
    let comics = list_comics_async(db_path).await.unwrap_or_else(|_| vec![]); // Simplified error handling
    Json(comics.into_iter().map(|c| ComicResponse { id: c.id, content: c.content }).collect())
}


struct ScanRequest {
    directory_path: String,
    db_path: String,
}
static db_path: String = ".".to_string();

async fn scan_directory_handler(Json(payload): Json<ScanRequest>) -> String {
    match modules::filehandler::scan_directory_and_store_comic_info_async(payload.directory_path, payload.db_path).await {
        Ok(_) => "Scan and storage successful".to_string(),
        Err(e) => format!("Error during scan and storage: {}", e),
    }
}

#[tokio::main]
async fn main() {
    // Define the Axum router with the route to list comics
    let app = Router::new()
    .route("/scan_directory", post(move || scan_directory_handler(db_path.clone())))
    .route("/list_comics", get(move || list_comics_handler(db_path.clone())));
    // Run our app with hyper on localhost at port 3000
    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Listening on {}", addr);
    server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}