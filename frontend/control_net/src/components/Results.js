import React from 'react';
import styled from 'styled-components';

const ResultsContainer = styled.div`
  margin-top: 20px;
`;

// const ResultImage = styled.img`
//   max-width: 100%;
//   margin-bottom: 10px;
// `;

const ResultImage = styled.img`
  width: 500px;
  height: 400px;
  margin: 0 auto 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  background-color: #f0f0f0;
  border-radius: 10px;
`;


function Results({ results }) {
  return (
    <ResultsContainer>
      <h2>처리 결과</h2>
      <p>처리 시간: {results.process_time}초</p>
      {results.output_paths.map((path, index) => (
        <div key={index}>
          {/* <ResultImage src={path} alt={`결과 이미지 ${index + 1}`} /> */}
          <ResultImage src={`http://localhost:8000/image/?file_path=${path}`} alt={`결과 이미지 ${index + 1}`} />

          <p>FID 점수 {index + 1}: {results.score_fid[index]}</p>
          <p>SSIM 점수 {index + 1}: {results.score_ssim[index]}</p>
        </div>
      ))}
    </ResultsContainer>
  );
}

export default Results;