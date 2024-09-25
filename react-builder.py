import os
import subprocess

def run_command(command):
    """Run a shell command and wait for it to complete."""
    process = subprocess.run(command, shell=True, check=True)
    return process.returncode

def create_react_app(project_name):
    # Step 1: Create Vite React app
    print(f"Creating Vite React app: {project_name}")
    run_command(f"npm create vite@latest {project_name} -- --template react")

    # Step 2: Navigate into the project directory
    os.chdir(project_name)

    # Step 3: Install required packages
    print("Installing dependencies...")
    run_command("npm install react-icons react-redux @reduxjs/toolkit tailwindcss postcss autoprefixer")

    # Step 4: Initialize Tailwind CSS
    run_command("npx tailwindcss init -p")

    # Step 5: Modify tailwind.config.js
    tailwind_config_content = """\
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        
      },
      fontFamily: {
        roboto: ['Roboto', 'sans-serif'],
        ropa: ['Ropa Sans', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
"""
    with open("tailwind.config.js", "w") as tailwind_config_file:
        tailwind_config_file.write(tailwind_config_content)
    print("Updated tailwind.config.js")

    # Step 6: Modify vite.config.js
    vite_config_content = """\
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
  }
})
"""
    with open("vite.config.js", "w") as vite_config_file:
        vite_config_file.write(vite_config_content)
    print("Updated vite.config.js")

    # Step 7: Remove app.css and update App.jsx
    if os.path.exists("src/App.css"):
        os.remove("src/App.css")
        print("Removed src/App.css")

    # Rewrite App.jsx
    app_jsx_content = """\
function App() {
  return (
    <>
      App Here
    </>
  )
}

export default App
"""
    with open("src/App.jsx", "w") as app_file:
        app_file.write(app_jsx_content)
    print("Rewritten src/App.jsx")

    # Step 8: Rewrite index.css
    index_css_content = """\
@tailwind base;
@tailwind components;
@tailwind utilities;
"""
    with open("src/index.css", "w") as index_css_file:
        index_css_file.write(index_css_content)
    print("Updated src/index.css")

    # Step 9: Create store.js
    store_js_content = """\
import { configureStore } from '@reduxjs/toolkit';

const store = configureStore({
    reducer: {

    },
});

export default store;
"""
    with open("src/store.js", "w") as store_file:
        store_file.write(store_js_content)
    print("Created src/store.js")

    # Step 10: Rewrite main.jsx
    main_jsx_content = """\
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'
import { StrictMode } from 'react'
import store from './store.js'
import App from './App.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </StrictMode>
)
"""
    with open("src/main.jsx", "w") as main_file:
        main_file.write(main_jsx_content)
    print("Updated src/main.jsx")

    # Step 11: Update index.html
    index_html_content = f"""\
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Ropa+Sans&display=swap" rel="stylesheet">
    <title>{project_name.replace('-', ' ')}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""
    with open("index.html", "w") as index_html_file:
        index_html_file.write(index_html_content)
    print("Updated index.html")

    # Step 12: Update README.md
    readme_content = f"# {project_name}\n"
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
    print(f"Updated README.md to contain '# {project_name}'")

    print("React app setup complete!")

if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_react_app(project_name)
