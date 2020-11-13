import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    margin: 0,
    marginBottom: 0,
    padding: 10,
    display: "flex",
    backgroundColor: "#192879",
    flex: 1,
    flexDirection: "column",
  },
  contactLabel: {
    textAlign: "center",
    fontSize: 35,
    color: 'white',
  },
  avatarStyle: {
    height: 50,
    width: 50,
    borderRadius: 25,
  },
  rowContainer: {
    alignItems: "center",
    display: "flex",
    flexDirection: "row",
  },
  textStyle: {
    fontSize: 15,
    color: 'white',
  }
});

export default styles;
