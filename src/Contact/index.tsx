import React from "react";
import { createStackNavigator } from "@react-navigation/stack";
import ContactScreen from "./ContactScreen";
import ContactDetail from "./ContactDetail";
import GroupScreen from "./GroupScreen";

const Stack = createStackNavigator();

export default function MenuStack():JSX.Element {
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
      <Stack.Screen
        name={"GroupScreen"}
        component={GroupScreen}
        options={{ headerShown: false }}
      />
    </Stack.Navigator>
  );
}
