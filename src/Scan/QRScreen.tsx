import React from "react";
import { Image, View, Text, StyleSheet } from "react-native";
import { QRCode } from "react-native-custom-qr-codes-expo";
import FAB from "../components/FAB";
import { Ionicons } from "@expo/vector-icons";
import user from "../../config/user";

export default function QRScreen({ navigation }: any) {
  return (
    <View style={styles.container}>
      <QRCode content={"impression://" + user.email} />

      <FAB
        onPress={() => {
          navigation.push("Scan");
        }}
      >
        <Ionicons
          name="md-qr-scanner"
          style={{ color: "white", fontSize: 30 }}
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
});
