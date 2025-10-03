Movie Explorer

This repository contains a Tornado-based backend and a Vite + Vue frontend.

Quick start

1. Install root dependencies:

```bash
npm install
```

- Frontend dependencies can be installed from the project root with:

  ```bash
  npm install --prefix frontend
  ```

- Backend dependencies are listed in `requirements.txt` (install with `pip install -r requirements.txt`).

2. Start the app (runs the Tornado API and the frontend dev server):

```bash
npm run dev
```

What this does

- `npm run dev` uses `concurrently` to run the Python API (`python api/app.py`) and the frontend dev server (`npm run dev --prefix frontend`).
- Backend: listens on http://localhost:8888 (see `api/docs/openapi: '3.0.yml`)
- Frontend: served by Vite (default http://localhost:5173)

Testing

Backend Tests:

```bash
# From the root directory
pytest
```

Frontend Tests:

```bash
# From the frontend directory
cd frontend && npm run test
```

Notes

- Make sure you have Python 3.10+ and Node.js (matching `frontend/package.json` engines) installed.
- For backend tests, ensure you have pytest installed (`pip install pytest`)
- Frontend tests use Vitest and can be run in watch mode with `npm run test`
