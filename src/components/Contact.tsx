import React from "react";
import "../Contact/ContactsStyle.tsx";
import { View, Text } from "react-native";

function Contact({ name }: { name: string }) {
   return (
      <View>
         <Text>{name}</Text>
      </View>
   );
}

export default Contact;
