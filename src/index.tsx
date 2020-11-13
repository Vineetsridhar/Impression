import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import React, { useState, useEffect } from "react";
import ProfileScreen from "./Profile/ProfileScreen";
import Contact from "./Contact";
import { Ionicons } from "@expo/vector-icons";
import Scan from "./Scan";
import Login from "./login";
import { AsyncStorage } from "react-native";
import user from "../config/user";

const Tab = createBottomTabNavigator();

export default function Tabs() {
  const [loggedIn, setLoggedIn] = useState(false);

  const checkLogin = async () => {
    //Never actually implement persistance like this im sorry
    const email = await AsyncStorage.getItem("email");
    if (email) {
      user.email = email;
      setLoggedIn(true);
    }
  };

  useEffect(() => {
    checkLogin();
  }, []);

  if (!loggedIn) return <Login setLoggedIn={setLoggedIn} />;

  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName: string;

          if (route.name === "Scan") {
            iconName = "md-qr-scanner";
          } else if (route.name === "Profile") {
            iconName = "md-person";
          } else {
            iconName = "md-people";
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
      })}
      initialRouteName={"Scan"}
    >
      <Tab.Screen name="Profile" component={ProfileScreen} />
      <Tab.Screen name="Scan" component={Scan} />
      <Tab.Screen name="Contacts" component={Contact} />
    </Tab.Navigator>
  );
}
