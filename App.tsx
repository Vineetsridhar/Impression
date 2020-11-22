import React from 'react';
import { StyleSheet } from 'react-native';
import Tabs from './src'
import { NavigationContainer } from '@react-navigation/native';
import { AppLoading } from 'expo';

import {
  useFonts,
  Blinker_400Regular,
  Blinker_600SemiBold
} from '@expo-google-fonts/blinker';

export default function App() {
  let [fontsLoaded] = useFonts({
    Blinker_400Regular,
    Blinker_600SemiBold
  });
  if (!fontsLoaded) {
    return <AppLoading />;
  }
  return (
    <NavigationContainer>
      <Tabs />
    </NavigationContainer>
  );
}