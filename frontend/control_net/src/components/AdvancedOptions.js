import React from 'react';
import styled from 'styled-components';

const OptionsContainer = styled.div`
  margin-bottom: 20px;
`;

const OptionGroup = styled.div`
  margin-bottom: 10px;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 5px;
`;

const Input = styled.input`
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
`;

const Checkbox = styled.input`
  margin-right: 5px;
`;

function AdvancedOptions({ options, setOptions }) {
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setOptions(prevOptions => ({
      ...prevOptions,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  return (
    <OptionsContainer>
      <h3>Advanced Option</h3>
      <OptionGroup>
        <Label>num samples</Label>
        <Input type="number" name="num_samples" value={options.num_samples} onChange={handleChange} />
      </OptionGroup>
      <OptionGroup>
        <Label>Canny image resolution</Label>
        <Input type="range" name="image_resolution" min="256" max="1024" value={options.image_resolution} onChange={handleChange} />
        <span>{options.image_resolution}</span>
      </OptionGroup>
      <OptionGroup>
        <Label>Canny high threshold</Label>
        <Input type="range" name="low_threshold" min="1" max="255" value={options.low_threshold} onChange={handleChange} />
        <span>{options.low_threshold}</span>
      </OptionGroup>
      <OptionGroup>
        <Label>Canny 상한 임계값</Label>
        <Input type="range" name="high_threshold" min="1" max="255" value={options.high_threshold} onChange={handleChange} />
        <span>{options.high_threshold}</span>
      </OptionGroup>
      <OptionGroup>
        <Label>Number of steps</Label>
        <Input type="number" name="num_steps" value={options.num_steps} onChange={handleChange} />
      </OptionGroup>
      <OptionGroup>
        <Label>Guidance scale</Label>
        <Input type="number" name="guidance_scale" value={options.guidance_scale} onChange={handleChange} step="0.1" />
      </OptionGroup>
      <OptionGroup>
        <Label>Seed</Label>
        <Input type="number" name="seed" value={options.seed} onChange={handleChange} />
      </OptionGroup>
      <OptionGroup>
        <Checkbox type="checkbox" name="randomize_seed" checked={options.randomize_seed} onChange={handleChange} />
        <Label>Random Seed</Label>
      </OptionGroup>
      <OptionGroup>
        <Label>Additional prompt</Label>
        <Input type="text" name="a_prompt" value={options.a_prompt} onChange={handleChange} />
      </OptionGroup>
      <OptionGroup>
        <Label>Negative prompt</Label>
        <Input type="text" name="n_prompt" value={options.n_prompt} onChange={handleChange} />
      </OptionGroup>
    </OptionsContainer>
  );
}

export default AdvancedOptions;