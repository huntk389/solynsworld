# CORE006 Memory Portal — DevKit v1

## Structure
- `backend/app.py`: Flask app for file uploads
- `frontend/index.html`: Upload form page
- `data/uploads/`: Where uploaded files are stored
- `docs/README.md`: This documentation

## Hosting Plan
- Backend: Render (Flask app)
- Frontend: Netlify (HTML upload)
- Repo: GitHub (main code + history)

## Instructions
1. Clone repo and deploy backend to Render.
2. Deploy static `frontend/` to Netlify.
3. Link Netlify form to backend endpoint on Render.
4. Upload files via form and check saved data at `/data/uploads`.

This is version 1. Future updates will include tag-based routing and file versioning UI.
