import './App.css'

function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>🎨 Your Personal Website Template</h1>
        <p>Ready to customize and deploy to AWS</p>
      </header>

      <main className="main">
        <section className="hero-card">
          <h2>👋 Welcome!</h2>
          <p>
            This is your personal website template, ready to be customized and deployed to AWS.
            Use Kiro to transform this template into your own unique website.
          </p>
        </section>

        <div className="steps-container">
          <div className="step-card">
            <div className="step-number">1</div>
            <h2>🤖 Customize with Kiro</h2>
            <p>Ask Kiro to personalize this website for you. Here are some example prompts:</p>
            <ul className="prompt-list">
              <li>"Create a portfolio website with my projects and contact info"</li>
              <li>"Make this a personal blog with an about me section"</li>
              <li>"Build a landing page for my freelance services"</li>
              <li>"Add a photo gallery and bio section"</li>
            </ul>
            <p className="tip">💡 Tip: Be specific about what you want - colors, sections, content, style, etc.</p>
          </div>

          <div className="step-card">
            <div className="step-number">2</div>
            <h2>🧪 Test Locally</h2>
            <p>Before deploying, test your website locally to see how it looks:</p>
            <div className="code-block">
              <code>npm install</code>
              <code>npm run dev</code>
            </div>
            <p className="note">
              🌐 Your site will be available at http://localhost:5173
              <br />
              Make changes and see them update instantly with hot reload!
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">3</div>
            <h2>⚙️ Setup AWS Environment</h2>
            <p>Prepare your environment for AWS deployment:</p>
            <div className="code-block">
              <code>cd cdk</code>
              <code>python3 -m venv .venv</code>
              <code>source .venv/bin/activate</code>
              <code>pip install -r requirements.txt</code>
              <code>npm install -g aws-cdk</code>
            </div>
            <p className="note">
              🔑 Configure AWS credentials with <code className="inline-code">aws configure</code>
              <br />
              📦 Bootstrap CDK (first time only): <code className="inline-code">cdk bootstrap</code>
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">4</div>
            <h2>🚀 Deploy to AWS</h2>
            <p>Once you're happy with your website, deploy it with these commands:</p>
            <div className="code-block">
              <code>npm run build</code>
              <code>cd cdk</code>
              <code>cdk deploy</code>
            </div>
            <p className="note">
              ✅ After deployment, your CloudFront URL will be displayed in the output.
              Your site will be hosted on CloudFront + S3.
            </p>
          </div>
        </div>

        <section className="tech-card">
          <h2>🛠️ Tech Stack</h2>
          <div className="tech-grid">
            <div className="tech-item">⚛️ React + TypeScript</div>
            <div className="tech-item">⚡ Vite for fast builds</div>
            <div className="tech-item">☁️ AWS CDK for infrastructure</div>
            <div className="tech-item">🌐 CloudFront + S3 for hosting</div>
            <div className="tech-item">🤖 Kiro for AI-powered customization</div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <p>Built with React + Vite + AWS CDK + Kiro</p>
      </footer>
    </div>
  )
}

export default App
