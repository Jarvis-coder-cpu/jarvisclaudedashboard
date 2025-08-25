export async function getStatusReport() {
  try {
    const response = await fetch('http://localhost:5001/status');
    if (response.ok) {
      const data = await response.json();
      return data;
    } else {
      throw new Error('Status fetch failed');
    }
  } catch (error) {
    console.warn('[STATUS] Backend unavailable, using fallback data');
    // Fallback data when backend is down
    return {
      identity: "Disconnected",
      kernel: "Backend Offline",
      last_verified: "Connection failed",
      tokens: 0,
      role: "Jarvis (Backend Offline)",
      drift: "No Connection",
      mode: "offline",
      ready_for_llm: false
    };
  }
}
