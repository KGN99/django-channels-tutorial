import React from "react";
import Chat from "./containers/Chat";
import WebSocketInstance from "./websocket";

export default class App extends React.Component {
  componentDidMount() {
    WebSocketInstance.connect();
  }

  render() {
    return <Chat />;
  }
}
