import { StyleSheet } from "react-native";
import colors from "../../config/colors";

const styles = StyleSheet.create({
  infoContainer: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  colContainer: {
    display: 'flex',
    flexDirection: "column",
    width: '100%',
    margin: 16
  },
  textStyle: {
    fontSize: 20,
    color: colors.text,
  },
  container: {
    margin: 0,
    display: 'flex',
    flexDirection: 'column',
    flex: 1,
    padding: 10,
    backgroundColor: colors.background,
  },
  contentContainer: {
    alignItems: 'center'
  },
  icon: {
    marginVertical: 16,
  },
  title: {
    fontSize: 30,
    color: colors.text,
    fontWeight: 'bold'
  },
  iconStyle: {
    width: 50
  },
  linksContainer: {
    display: 'flex',
    flexDirection: 'row',
    width: '100%',
    justifyContent: 'space-evenly'
  },
  link: {
    fontSize: 20,
    color: colors.main,
    paddingVertical: 16
  }
});

export default styles;
