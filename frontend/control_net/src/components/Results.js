import React from 'react';
import styled from 'styled-components';

const ResultsContainer = styled.div`
  margin-top: 20px;
`;

const ResultImage = styled.img`
  max-width: 100%;
  margin-bottom: 10px;
`;

function Results({ results }) {
  return (
    <ResultsContainer>
      <h2>처리 결과</h2>
      <p>처리 시간: {results.process_time}초</p>
      <p>FID 점수: {results.fid_score}</p>
      <p>FSNR 점수: {results.fsnr_score}</p>
      <p>SSIM 점수: {results.ssim_score}</p>
      {results.output_paths.map((path, index) => (
        <ResultImage key={index} src={path} alt={`결과 이미지 ${index + 1}`} />
      ))}
    </ResultsContainer>
  );
}

export default Results;