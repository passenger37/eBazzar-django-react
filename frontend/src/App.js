import { useEffect, useState } from 'react';
import './App.css';
import Home from './pages/Home';
import Login from './pages/Login';
import Signup from './pages/Signup';

function App() {
  const [path, setPath] = useState(window.location.pathname);

  useEffect(() => {
    const handlePopState = () => setPath(window.location.pathname);
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  const navigate = (newPath) => {
    if (newPath === path) return;
    window.history.pushState({}, '', newPath);
    setPath(newPath);
  };

  const renderPage = () => {
    if (path === '/login') return <Login />;
    if (path === '/signup') return <Signup />;
    return <Home />;
  };

  return (
    <div className="app">
      <nav className="navbar">
        <div className="brand">eBazzar</div>
        <div className="nav-actions">
          {/* {path === '/login' && (
            <a
              href="/signup"
              className="nav-link nav-link-primary"
              onClick={(event) => {
                event.preventDefault();
                navigate('/signup');
              }}
            >
              Signup
            </a>
          )} */}
          {/* {path === '/signup' && (
            <a
              href="/login"
              className="nav-link"
              onClick={(event) => {
                event.preventDefault();
                navigate('/login');
              }}
            >
              Login
            </a>
          )} */}
          {path === '/' && (
            <a
              href="/signup"
              className="nav-link nav-link-primary"
              onClick={(event) => {
                event.preventDefault();
                navigate('/signup');
              }}
            >
              Signup
            </a>
          )}
        </div>
      </nav>

      {renderPage()}
    </div>
  );
}

export default App;
