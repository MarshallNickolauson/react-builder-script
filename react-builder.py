import os
import subprocess
import webbrowser
import time

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
    run_command("npm install react-icons react-redux @reduxjs/toolkit tailwindcss postcss autoprefixer react-router-dom react-spinners")

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
import { Route, createBrowserRouter, createRoutesFromElements, RouterProvider } from 'react-router-dom'
import MainLayout from './layouts/MainLayout'
import NotFoundPage from './pages/NotFoundPage';
import HomePage from './pages/HomePage';

function App() {

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path='/' element={<MainLayout />} >
        <Route index element={<HomePage />} />
        <Route path='*' element={<NotFoundPage />} />
      </Route>
    )
  );

  return <RouterProvider router={router} />;
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
    readme_content = "# Project name\n"
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
    print("Updated README.md to contain '# Project name'")

    # Step 13: Create pages directory and HomePage.jsx and NotFoundPage.jsx
    os.makedirs("src/pages", exist_ok=True)

    home_page_content = """\
const HomePage = () => {
  return (
    <>
      HomePage
    </>
  )
}

export default HomePage
"""
    with open("src/pages/HomePage.jsx", "w") as home_file:
        home_file.write(home_page_content)
    print("Created src/pages/HomePage.jsx")

    not_found_page_content = """\
import { Link } from 'react-router-dom'

const NotFoundPage = () => {
    return (
        <section className='text-center flex flex-col justify-center items-center h-96'>
            <h1 className='text-6xl font-bold mb-4'>404 Not Found</h1>
            <p className='text-xl mb-5'>This page does not exist</p>
            <Link
                to='/'
                className='text-white bg-orange-400 hover:bg-orange-500 rounded-full px-3 py-3 mt-4'
            >
                Go Back
            </Link>
        </section>
    )
}

export default NotFoundPage
"""
    with open("src/pages/NotFoundPage.jsx", "w") as not_found_file:
        not_found_file.write(not_found_page_content)
    print("Created src/pages/NotFoundPage.jsx")

    # Step 14: Create layouts directory and MainLayout.jsx
    os.makedirs("src/layouts", exist_ok=True)

    main_layout_content = """\
import React from 'react'
import Navbar from '../components/Navbar'
import { Outlet } from 'react-router-dom';
import Footer from '../components/Footer';

const MainLayout = () => {
  return (
    <>
      <Navbar />
      <Outlet />
      <Footer />
    </>
  );
};
export default MainLayout;
"""
    with open("src/layouts/MainLayout.jsx", "w") as main_layout_file:
        main_layout_file.write(main_layout_content)
    print("Created src/layouts/MainLayout.jsx")

    # Step 15: Create components directory and Navbar and Footer components
    os.makedirs("src/components", exist_ok=True)

    navbar_content = """\
function Navbar() {
  return (
    <nav>
      navbar
    </nav>
  );
}

export default Navbar;
"""
    with open("src/components/Navbar.jsx", "w") as navbar_file:
        navbar_file.write(navbar_content)
    print("Created src/components/Navbar.jsx")

    footer_content = """\
function Footer() {
  return (
    <footer>
      footer
    </footer>
  );
}

export default Footer;
"""
    with open("src/components/Footer.jsx", "w") as footer_file:
        footer_file.write(footer_content)
    print("Created src/components/Footer.jsx")

    # Step 16: Delete react.svg from src/assets
    react_svg_path = "src/assets/react.svg"
    if os.path.exists(react_svg_path):
        os.remove(react_svg_path)
        print("Removed src/assets/react.svg")

    # Final message
    print("React app setup complete!")
    
    # Step 17: Run the development server
    print("Starting the development server...")
    subprocess.Popen("npm run dev", shell=True)
    time.sleep(1)
    
    # Step 18: Open the default web browser to the localhost URL
    webbrowser.open("http://localhost:3000/")

if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_react_app(project_name)
