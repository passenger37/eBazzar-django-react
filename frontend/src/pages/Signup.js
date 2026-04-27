import React from 'react';

function Signup() {
  return (
    <main className="auth-page">
      <h2>Create an account</h2>
      <p>Signup to start buying and selling products on eBazzar.</p>

      <div className="auth-field">
        <label htmlFor="signup-name">Full Name</label>
        <input id="signup-name" type="text" placeholder="Your name" />
      </div>

      <div className="auth-field">
        <label htmlFor="signup-email">Email</label>
        <input id="signup-email" type="email" placeholder="you@example.com" />
      </div>

      <div className="auth-field">
        <label htmlFor="signup-password">Password</label>
        <input id="signup-password" type="password" placeholder="Create a password" />
      </div>

      <button className="auth-button">Signup</button>

      <p className="auth-note">
        Already have an account? <a className="auth-link" href="/login">Login</a>
      </p>
    </main>
  );
}

export default Signup;
