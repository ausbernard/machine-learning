import React, { useState, useRef } from 'react';

const AlgorithmVisualizer = () => {
  const [speed, setSpeed] = useState(1.0);
  const [target, setTarget] = useState('');
  const [message, setMessage] = useState('Algorithm Visualizer');
  const [algorithm, setAlgorithm] = useState('DFS');
  const [targetFound, setTargetFound] = useState(false);
  const [path, setPath] = useState([]);
  const canvasRef = useRef(null);

  const drawGraph = (graph, visited, current, target, path) => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const nodeRadius = 20;
    const positions = [
      { x: 100, y: 100 }, { x: 200, y: 100 }, { x: 300, y: 100 }, { x: 400, y: 100 }, { x: 500, y: 100 },
      { x: 600, y: 100 }, { x: 100, y: 200 }, { x: 200, y: 200 }, { x: 300, y: 200 }, { x: 400, y: 200 },
      { x: 500, y: 200 }, { x: 600, y: 200 }, { x: 100, y: 300 }, { x: 200, y: 300 }, { x: 300, y: 300 },
      { x: 400, y: 300 }, { x: 500, y: 300 }, { x: 600, y: 300 }, { x: 100, y: 400 }, { x: 200, y: 400 },
      { x: 300, y: 400 }, { x: 400, y: 400 }, { x: 500, y: 400 },
    ];

    // Draw edges
    graph.forEach((neighbors, node) => {
      neighbors.forEach((neighbor) => {
        const { x: x0, y: y0 } = positions[node];
        const { x: x1, y: y1 } = positions[neighbor];
        ctx.beginPath();
        ctx.moveTo(x0, y0);
        ctx.lineTo(x1, y1);
        ctx.strokeStyle = 'black';
        ctx.stroke();
      });
    });

    // Draw nodes
    graph.forEach((_, node) => {
      const { x, y } = positions[node];
      ctx.beginPath();
      ctx.arc(x, y, nodeRadius, 0, 2 * Math.PI);
      if (node === target && targetFound) {
        ctx.fillStyle = 'pink';
      } else if (path.includes(node)) {
        ctx.fillStyle = 'yellow';
      } else if (visited[node]) {
        ctx.fillStyle = node === current ? 'red' : 'lime';
      } else {
        ctx.fillStyle = 'blue';
      }
      ctx.fill();
      ctx.strokeStyle = 'black';
      ctx.stroke();
      ctx.fillStyle = 'black';
      ctx.fillText(node, x - 5, y + 5);
    });
  };

  const reconstructPath = (parent, target) => {
    const path = [];
    let current = target;
    while (current !== null) {
      path.push(current);
      current = parent[current];
    }
    return path.reverse();
  };

  const dfs = async (graph, start, target) => {
    const visited = Array(graph.length).fill(false);
    const parent = Array(graph.length).fill(null);
    const stack = [start];

    while (stack.length > 0) {
      const node = stack.pop();
      if (!visited[node]) {
        visited[node] = true;
        drawGraph(graph, visited, node, target, []);
        await new Promise((resolve) => setTimeout(resolve, 1000 / speed));

        if (node === target) {
          setTargetFound(true);
          const path = reconstructPath(parent, target);
          setPath(path);
          drawGraph(graph, visited, node, target, path); // Ensure target is highlighted
          return node;
        }

        for (const neighbor of graph[node]) {
          if (!visited[neighbor]) {
            parent[neighbor] = node;
            stack.push(neighbor);
          }
        }
      }
    }

    return -1;
  };

  const bfs = async (graph, start, target) => {
    const visited = Array(graph.length).fill(false);
    const parent = Array(graph.length).fill(null);
    const queue = [start];

    while (queue.length > 0) {
      const node = queue.shift();
      if (!visited[node]) {
        visited[node] = true;
        drawGraph(graph, visited, node, target, []);
        await new Promise((resolve) => setTimeout(resolve, 1000 / speed));

        if (node === target) {
          setTargetFound(true);
          const path = reconstructPath(parent, target);
          setPath(path);
          drawGraph(graph, visited, node, target, path); // Ensure target is highlighted
          return node;
        }

        for (const neighbor of graph[node]) {
          if (!visited[neighbor]) {
            parent[neighbor] = node;
            queue.push(neighbor);
          }
        }
      }
    }

    return -1;
  };

  const startVisualization = async () => {
    const graph = [
      [1, 6], [0, 2, 7], [1, 3, 8], [2, 4, 9], [3, 5, 10], [4, 11],
      [0, 7, 12], [1, 6, 8, 13], [2, 7, 9, 14], [3, 8, 10, 15], [4, 9, 11, 16],
      [5, 10, 17], [6, 13, 18], [7, 12, 14, 19], [8, 13, 15, 20], [9, 14, 16, 21],
      [10, 15, 17, 22], [11, 16], [12, 19], [13, 18, 20], [14, 19, 21], [15, 20, 22], [16, 21]
    ];
    const targetNum = parseInt(target, 10);

    if (isNaN(targetNum) || targetNum < 0 || targetNum >= graph.length) {
      setMessage('Please enter a valid node number');
      return;
    }

    setTargetFound(false); // Reset target found state
    setPath([]); // Reset path
    let result;
    if (algorithm === 'DFS') {
      result = await dfs(graph, 0, targetNum);
    } else {
      result = await bfs(graph, 0, targetNum);
    }

    if (result !== -1) {
      setMessage(`Node ${result} found`);
    } else {
      setMessage('Node not found');
    }
  };

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <h1>{message}</h1>
      <canvas ref={canvasRef} width="700" height="500" style={{ backgroundColor: 'white', margin: '20px auto' }}></canvas>
      <div>
        <button onClick={startVisualization}>Start</button>
      </div>
      <div>
        <label>Speed</label>
        <input
          type="range"
          min="0.1"
          max="3.0"
          step="0.5"
          value={speed}
          onChange={(e) => setSpeed(parseFloat(e.target.value))}
        />
      </div>
      <div>
        <label>Node to Find</label>
        <input
          type="text"
          value={target}
          onChange={(e) => setTarget(e.target.value)}
        />
      </div>
      <div>
        <label>
          <input
            type="radio"
            value="DFS"
            checked={algorithm === 'DFS'}
            onChange={(e) => setAlgorithm(e.target.value)}
          />
          DFS
        </label>
        <label>
          <input
            type="radio"
            value="BFS"
            checked={algorithm === 'BFS'}
            onChange={(e) => setAlgorithm(e.target.value)}
          />
          BFS
        </label>
      </div>
    </div>
  );
};

export default AlgorithmVisualizer;