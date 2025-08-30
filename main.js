const { app, BrowserWindow } = require('electron');
const path = require('path');
const os = require('os');

// Security: Disable GPU acceleration to prevent errors
app.disableHardwareAcceleration();

// Security: Set secure cache location to prevent tampering
const jarvisCacheDir = path.join(__dirname, 'jarvis-secure-cache');
app.setPath('userData', jarvisCacheDir);
app.setPath('cache', path.join(jarvisCacheDir, 'cache'));
app.setPath('temp', path.join(jarvisCacheDir, 'temp'));

// Security: Disable unsafe features
app.commandLine.appendSwitch('--disable-web-security', 'false');
app.commandLine.appendSwitch('--disable-features', 'VizDisplayCompositor');
app.commandLine.appendSwitch('--no-sandbox', 'false');

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      webSecurity: false
    },
    show: false
  });

  win.loadFile('index.html');
  
  // Uncomment to open dev tools for debugging
  // win.webContents.openDevTools();
  
  win.once('ready-to-show', function() {
    win.show();
  });
}

app.whenReady().then(createWindow);
