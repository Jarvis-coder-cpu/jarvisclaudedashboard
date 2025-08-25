const { app, BrowserWindow } = require('electron');
const path = require('path');

// Disable GPU acceleration to prevent errors
app.disableHardwareAcceleration();

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      nodeIntegration: true
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
