#!/bin/bash

# Chess Project - Build and Start Script
# This script builds the CSS and starts the local development server

echo "🚀 Starting Chess Project..."
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Step 1: Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
    echo ""
fi

# Step 2: Build Tailwind CSS
echo "🎨 Building CSS..."
npm run build:css
echo "✅ CSS built successfully"
echo ""

# Step 3: Kill any existing processes serving this project
echo "🔍 Checking for existing processes..."
killed_any=false

for port in {8000..8100}; do
    # Check if port is in use
    pid=$(lsof -Pi :$port -sTCP:LISTEN -t 2>/dev/null)
    
    if [ ! -z "$pid" ]; then
        # Check the working directory of the process
        process_cwd=$(lsof -a -p $pid -d cwd -Fn 2>/dev/null | grep '^n' | cut -c2-)
        frontend_path="$SCRIPT_DIR/frontend"
        
        # If it's serving from our project directory, kill it
        if [ "$process_cwd" = "$frontend_path" ] || [ "$process_cwd" = "$SCRIPT_DIR" ]; then
            echo "  ⏹️  Stopping existing server on port $port (PID: $pid)..."
            kill $pid 2>/dev/null
            killed_any=true
            # Give it a moment to shut down
            sleep 0.5
        fi
    fi
done

if [ "$killed_any" = true ]; then
    echo "  ✅ Existing processes stopped"
    echo ""
fi

# Step 4: Start fresh server on port 8000
port=8000

echo "🌐 Starting development server..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✨ Chess Project is running!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  📍 Local:   http://localhost:$port"
echo "  📂 Serving: ./"
echo ""
echo "  ♟️ Open this link http://localhost:$port/frontend/index.html to play the game!"
echo ""
echo "  Press Ctrl+C to stop the server"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Python HTTP server in the root directory
python3 -m http.server $port
