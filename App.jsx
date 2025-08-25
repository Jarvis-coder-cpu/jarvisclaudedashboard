 import React, { useState, useEffect } from 'react';
import { interpretGlyphs } from './echolex_panel';
import { getPromptReflection } from './mirror';
import { getStatusReport } from './status';

function App() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('Awaiting command, sir.');
  const [glyphs, setGlyphs] = useState([]);
  const [reflection, setReflection] = useState('');
  const [status, setStatus] = useState({});

  const handleCommand = async () => {
    if (!input.trim()) return;
    setOutput('Processing...');
    setReflection(getPromptReflection(input));
    setGlyphs(interpretGlyphs(input));

    try {
      const res = await fetch('http://localhost:5001/command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: input })
      });
      const data = await res.json();
      setOutput(data.reply || 'No response.');
      setGlyphs(interpretGlyphs(data.reply));
    } catch (err) {
      setOutput('Error: Could not reach Jarvis core.');
    }

    updateStatus();
  };

  const updateStatus = async () => {
    const statusData = await getStatusReport();
    setStatus(statusData);
  };

  useEffect(() => {
    updateStatus();
    // Update status every 10 seconds
    const statusInterval = setInterval(updateStatus, 10000);
    return () => clearInterval(statusInterval);
  }, []);

  return (
    <div style={{ fontFamily: 'monospace', background: '#111', color: '#0f0', padding: '20px' }}>
      <h2>Jarvis Command</h2>
      <textarea
        rows={4}
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Enter your command here..."
        style={{ width: '100%', padding: '10px', borderRadius: '8px' }}
      />
      <button onClick={handleCommand} style={{ marginTop: '10px', width: '100%', padding: '10px', background: '#0f0', color: '#000', borderRadius: '8px' }}>
        Execute
      </button>

      <div style={{ marginTop: '20px', background: '#222', padding: '10px', borderRadius: '8px' }}>
        <strong>🧠 Response:</strong>
        <pre style={{ whiteSpace: 'pre-wrap' }}>{output}</pre>
      </div>

      <div style={{ marginTop: '10px', background: '#1a1a1a', padding: '10px', borderRadius: '8px' }}>
        <strong>🔁 Reflection:</strong> <code>{reflection}</code>
      </div>

      <div style={{ marginTop: '10px', background: '#1a1a1a', padding: '10px', borderRadius: '8px' }}>
        <strong>🜂 Symbolic Interpretation:</strong>
        <ul>
          {glyphs.map((g, i) => (
            <li key={i}>{g.glyph} — {g.meaning} ({g.role})</li>
          ))}
        </ul>
      </div>

      <div style={{ marginTop: '10px', background: '#000', padding: '10px', borderRadius: '8px' }}>
        <strong>🧾 System Status:</strong>
        <ul>
          <li>Identity: {status.identity}</li>
          <li>Kernel: {status.kernel}</li>
          <li>Last Verification: {status.last_verified}</li>
          <li>Tokens (est): {status.tokens}</li>
          <li>Role: {status.role}</li>
          <li>Drift Status: {status.drift}</li>
        </ul>
      </div>
    </div>
  );
}

export default App;
