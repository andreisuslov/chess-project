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

# Step 3: Find an available port or check if this project is already running
find_available_port() {
    local port=$1
    local max_port=$((port + 100))  # Try up to 100 ports
    
    while [ $port -lt $max_port ]; do
        # Check if port is in use
        if ! lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
            echo $port
            return 0
        fi
        
        # Port is in use, check if it's serving this project
        local pid=$(lsof -Pi :$port -sTCP:LISTEN -t)
        if [ ! -z "$pid" ]; then
            # Check the working directory of the process
            local process_cwd=$(lsof -a -p $pid -d cwd -Fn | grep '^n' | cut -c2-)
            local frontend_path="$SCRIPT_DIR/frontend"
            
            # If it's serving from our frontend directory, this project is already running
            if [ "$process_cwd" = "$frontend_path" ] || [ "$process_cwd" = "$SCRIPT_DIR" ]; then
                echo "ALREADY_RUNNING:$port"
                return 0
            fi
        fi
        
        port=$((port + 1))
    done
    
    echo "NONE"
    return 1
}

# Find available port starting from 8000
result=$(find_available_port 8000)

if [[ $result == ALREADY_RUNNING:* ]]; then
    # Extract the port number
    port=${result#ALREADY_RUNNING:}
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  ✨ Chess Project is already running!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "  📍 Local:   http://localhost:$port"
    echo "  📂 Serving: ./"
    echo ""
    echo "  ℹ️  Your CSS has been rebuilt with the latest changes"
    echo "  ℹ️  Just refresh your browser to see updates"
    echo ""
    echo "  ♟️ Open this link http://localhost:$port/frontend/index.html to play the game!"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
elif [ "$result" = "NONE" ]; then
    echo "❌ Error: Could not find an available port (tried 8000-8100)"
    exit 1
else
    # Start the server on the available port
    port=$result
    
    if [ $port -ne 8000 ]; then
        echo "ℹ️  Port 8000 is in use by another project"
        echo "ℹ️  Using port $port instead"
        echo ""
    fi
    
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
    # cd frontend  <-- Removed to serve from root
    python3 -m http.server $port
fi
