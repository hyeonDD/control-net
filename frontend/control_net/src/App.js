import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Game from './Game';
import ImageProcessor from './components/ImageProcessor';
import ReportPage from './components/ReportPage';

const Home = () => (
  <div className="home">
    <h1>이미지 처리 앱에 오신 것을 환영합니다</h1>
    <nav>
      <ul>
        <li>
          <Link to="/game">
            <button className="navigate-button">게임으로 이동</button>
          </Link>
        </li>
        <li>
          <Link to="/image-processor">
            <button className="navigate-button">이미지 처리</button>
          </Link>
        </li>
        <li>
          <Link to="/report">
            <button className="navigate-button">처리 결과 보기</button>
          </Link>
        </li>
      </ul>
    </nav>
  </div>
);

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/game" element={<Game />} />
        <Route path="/image-processor" element={<ImageProcessor />} />
        <Route path="/report" element={<ReportPage />} />
      </Routes>
    </Router>
  );
};

export default App;