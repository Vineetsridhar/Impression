import React from "react";
import { Image, View, StyleSheet } from "react-native";
import FAB from "../components/FAB";
import { Ionicons } from "@expo/vector-icons";
import user from "../../config/user";

export default function QRScreen({ navigation }: any):JSX.Element {
  return (
    <View style={styles.container}>
      <Image
        source={{
          uri: `https://impression-app.s3.amazonaws.com/${user.email.replace(
            "@",
            "%40"
          )}/qr.png`,
        }}
        style={styles.image}
      />

      <FAB
        onPress={() => {
          navigation.push("Scan");
        }}
      >
        <Ionicons
          name="md-qr-scanner"
          style={{ color: 'white', fontSize: 30 }}
        />
      </FAB>
    </View>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  image: {
    height: 300,
    width: 300,
  },
});
