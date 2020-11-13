import socketIO from "socket.io-client";

const socket = socketIO("http://192.168.2.15:8080", {
  transports: ["websocket"],
});

export default socket;
