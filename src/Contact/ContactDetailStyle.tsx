import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  scrollView: {
    height: "100%",
    width: "100%",
    alignSelf: "center",
  },
  infoContainer: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  rowContainer: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  },
  textStyle: {
    fontSize: 20,
    color: "white",
  },
  container: {
    margin: 0,
    flex: 1,
    padding: 10,
    backgroundColor: "#192879",
  },
  icon: {
    marginVertical: 16,
  },
});

export default styles;
