import React from 'react';

function Login() {
  return (
    <main className="auth-page">
      <h2>Login to eBazzar</h2>
      <p>Enter your credentials to continue shopping and managing your account.</p>

      <div className="auth-field">
        <label htmlFor="login-email">Email</label>
        <input id="login-email" type="email" placeholder="you@example.com" />
      </div>

      <div className="auth-field">
        <label htmlFor="login-password">Password</label>
        <input id="login-password" type="password" placeholder="Enter your password" />
      </div>

      <button className="auth-button">Login</button>

      <p className="auth-note">
        Don't have an account? <a className="auth-link" href="/signup">Signup now</a>
      </p>
    </main>
  );
}

export default Login;
