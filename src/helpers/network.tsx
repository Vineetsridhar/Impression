import user from "../../config/user";
import { LinkedInToken } from "react-native-linkedin";

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

export function linkedinLogin(authorizationCode: LinkedInToken) {
  return fetch(`${url}/linkedin_login`, getCallParams({ authorization_token: authorizationCode }))
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

export function deleteConnection(email: string) {
  return fetch(
    `${url}/delete_connection`,
    getCallParams({ user1_email: user.email, user2_email: email })
  );
}

export function batchNewUsers(emails:{user1_email:string, user2_email:string}[]){
  return fetch(
    `${url}/batch_new_users`,
    getCallParams(emails)
  )
}

export function editUser(user: any) {
  return fetch(`${url}/edit_user`, getCallParams(user));
}

export function uploadDocument(file: any) {
  const body = new FormData();
  body.append('file', {
    uri: file.uri,
    type: `application/pdf`,
    name: file.name
  });

  body.append("email", user.email)

  return fetch(
    `${url}/upload_doc`,
    {
      method: 'POST',
      body,
    }
  ).catch(err => {
    console.log(err)
  })
}

export function newGroup(groupName: string, emails: string[]) {
  return fetch(
    `${url}/new_group`,
    getCallParams({ emails, group_name: groupName })
  );
}

export function getGroups(email: string) {
  return fetch(
    `${url}/get_groups`,
    getCallParams({ email })
  );
}

export function getUserFromGroups(groupName: string) {
  return fetch(
    `${url}/get_users`,
    getCallParams({ group_name: groupName })
  );
}

export function getNearbyUsers(email: string, coordinates: any) {
  return fetch(
    `${url}/get_nearby_users`,
    getCallParams({ email, ...coordinates })
  )
}


export function uploadGroupDocument(file: any) {
  const body = new FormData();
  body.append('file', {
    uri: file.uri,
    type: `application/pdf`,
    name: file.name
  });

  body.append("email", user.email)

  return fetch(
    `${url}/upload_group_doc`,
    {
      method: 'POST',
      body,
    }
  )
}