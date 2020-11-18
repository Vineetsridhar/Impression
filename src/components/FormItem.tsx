import React from "react";
import { View, Text, TextInput, StyleSheet } from "react-native";
import colors from "../../config/colors";

interface props {
  title: string;
  onChangeText: (text: string) => void;
  value: string;
  placeholder: string;
  style?: any;
}

export default function FormItem({
  title,
  placeholder,
  style,
  value,
  onChangeText,
}: props) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
      <TextInput
        multiline
        style={[styles.inputStyle, style]}
        placeholder={placeholder}
        placeholderTextColor={colors.text}
        value={value}
        onChangeText={onChangeText}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "100%",
    alignItems: "center",
  },
  inputStyle: {
    width: "95%",
    height: 50,
    borderWidth: 1,
    marginHorizontal: 8,
    paddingHorizontal: 8,
    borderRadius: 10,
    color: 'black',
    borderColor: colors.borderColor,
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    width: "95%",
    marginVertical: 8,
  },
});
