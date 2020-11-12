import React from "react";
import { createStackNavigator } from "@react-navigation/stack";
import ContactScreen from "./ContactScreen";
import ContactList from "../components/ContactList";
import ContactDetail from "./ContactDetail";

const Stack = createStackNavigator();

export default function MenuStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name={"Contacts"}
        component={ContactScreen}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name={"ContactDetail"}
        component={ContactDetail}
        options={{ headerShown: false }}
      />
    </Stack.Navigator>
  );
}
