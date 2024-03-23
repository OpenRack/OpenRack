use axum::{routing::get, Router};

pub fn routes() -> Router {
    Router::new()
        .route("/", get(|| async { "Hello, World!" }))
        .route("/library", get(|| async { "Hello, Library!" }))
}