const API_URL = "http://13.204.63.146:8000";

async function apiGet(endpoint) {
  const response = await fetch(
    `${API_URL}${endpoint}`
  );

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`
    );
  }

  return response.json();
}

async function apiPost(
  endpoint,
  body
) {
  const response = await fetch(
    `${API_URL}${endpoint}`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify(body),
    }
  );

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`
    );
  }

  return response.json();
}

async function apiUpload(
  endpoint,
  formData
) {
  const response = await fetch(
    `${API_URL}${endpoint}`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`
    );
  }

  return response.json();
}
