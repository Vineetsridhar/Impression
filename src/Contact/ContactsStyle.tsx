import { StyleSheet } from "react-native";
import colors from "../../config/colors";
import font from "../../config/font"

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
    fontFamily: font.regular,
    color: colors.text,
  },
  avatarStyle: {
    height: 60,
    width: 60,
    borderRadius: 30,
    marginHorizontal: 8
  },
  rowContainer: {
    alignItems: "center",
    display: "flex",
    flexDirection: "row",
    width: '100%',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  textStyle: {
    fontSize: 15,
    color: colors.text,
    fontFamily: font.regular,
  },
  mainTextStyle: {
    fontSize: 20,
    color: colors.text,
    fontFamily: font.bold,

  },
  title: {
    width: '100%',
    textAlign: 'center',
    fontSize: 25,
    fontFamily: font.bold,

  },
  innerContainer: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center'
  }
});

export default styles;
