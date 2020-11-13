import user from "../../config/user";
import { User } from "./interfaces";

const url = "https://njit-cs490-project3-impression.herokuapp.com";

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

export function newConnection(email: string) {
  return fetch(
    `${url}/new_connection`,
    getCallParams({ user1_email: user.email, user2_email: email })
  );
}

export function editUser(user: any) {
  return fetch(`${url}/edit_user`, getCallParams(user));
}
