# Legal AI WebApp

Minimal Streamlit app for legal document analysis using Anthropic Claude.

## Files

- `app.py` - public version
- `app_private.py` - password-protected version
- `requirements.txt` - Python dependencies
- `.streamlit/secrets.toml.example` - example secrets file

## Run locally

1. Clone or download this project.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create `.streamlit/secrets.toml` from the example file:
   ```toml
   ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_API_KEY"
   APP_PASSWORD = "your-team-password"
   ```
5. Start the public app:
   ```bash
   streamlit run app.py
   ```
6. Or start the private app:
   ```bash
   streamlit run app_private.py
   ```

## Deploy to Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub.
4. Click **New app**.
5. Select the repository, branch, and main file:
   - Public app: `app.py`
   - Private app: `app_private.py`
6. Click **Advanced settings**.
7. In **Secrets**, paste:
   ```toml
   ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_API_KEY"
   APP_PASSWORD = "your-team-password"
   ```
8. Click **Deploy**.

## Set API key in Streamlit Cloud secrets

Use the app settings or Advanced settings during deploy and add:

```toml
ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_API_KEY"
APP_PASSWORD = "your-team-password"
```

The public app only requires `ANTHROPIC_API_KEY`. The private app requires both values.

## Switch between public and private version

- For a public app, deploy `app.py` as the main file.
- For a private team-only app, deploy `app_private.py` as the main file.
- You can create two separate Streamlit apps from the same repository if needed.

## Notes

- Streamlit Community Cloud is free for public repositories/apps.
- No database is required.
- Replace the placeholder API key with the real Anthropic key before production use.
