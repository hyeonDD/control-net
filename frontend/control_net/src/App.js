import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Game from './Game'; // 게임 컴포넌트 import

const Home = () => (
  <div className="home">
    <h1>Welcome to the App</h1>
    <Link to="/game">
      <button className="navigate-button">Go to Game</button>
    </Link>
  </div>
);

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/game" element={<Game />} />
        {/* 다른 경로가 필요하면 여기에 추가할 수 있습니다 */}
      </Routes>
    </Router>
  );
};

export default App;
