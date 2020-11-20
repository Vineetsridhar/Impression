import { StyleSheet } from "react-native";
import colors from "../../config/colors";

const styles = StyleSheet.create({
  container: {
    margin: 0,
    marginBottom: 0,
    marginTop: 10,
    display: "flex",
    backgroundColor: colors.background,
    flex: 1,
    flexDirection: "column",
  },
  contactLabel: {
    textAlign: "center",
    fontSize: 35,
    color: colors.text,
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
    color: colors.text,
  },
  title: {
    width: '100%',
    textAlign: 'center',
    fontSize: 25,
    fontWeight: 'bold'
  }
});

export default styles;
