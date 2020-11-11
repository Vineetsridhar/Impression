const url = "http://192.168.2.15:8080";

export function getCallParams(body: any) {
  return {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  };
}

export function newUser(data: any) {
  return fetch(`${url}/new_user`, getCallParams(data));
}

export function getUserInfo(email: string) {
  return fetch(`${url}/get_user`, getCallParams({ email }));
}

export function getConnections(email: string) {
  return fetch(
    `${url}/query_connections`,
    getCallParams({ user_email: email })
  );
}
