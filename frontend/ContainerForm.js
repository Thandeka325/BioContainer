#!/usr/bin/env node

import React, { useState } from "react";
import axios from "axios";

const ContainerForm = () => {
  const [formData, setFormData] = useState({
    os: "",
    software: "",
    resources: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:8000/api/containers", formData);
    console.log(response.data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="os" placeholder="Base OS" onChange={handleChange} required />
      <input name="software" placeholder="Software" onChange={handleChange} required />
      <input name="resources" placeholder="Resources (CPU, RAM, Storage)" onChange={handleChange} required />
      <button type="submit">Generate Container</button>
    </form>
  );
};

export default ContainerForm;


const [containerConfig, setContainerConfig] = useState("");

const handleSubmit = async (e) => {
	e.preventDefault();
	const response = await axios.post("http://localhost:8000/api/containers", formData);
	setContainerConfig(response.data.dockerfile);
};

return (
	<div>
	<form onSubmit={handleSubmit}>
	{/* Form Inputs */}
	</form>
	{containerConfig && (
		<pre>
		<code>{containerConfig}</code>
		</pre>
	)}
	</div>
);
