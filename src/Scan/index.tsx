import React from 'react'
import { createStackNavigator } from '@react-navigation/stack';
import ScanScreen from './ScanScreen';
import QRScreen from './QRScreen';

const Stack = createStackNavigator();

export default function MenuStack() {
    return (
        <Stack.Navigator>
            <Stack.Screen name={"Scan"} component={ScanScreen} options={{ headerShown: false }} />
            <Stack.Screen name={"QRCode"} component={QRScreen} options={{ headerShown: false }} />
        </Stack.Navigator>
    )
}