import React from 'react';
import { View, Text } from 'react-native';
import styles from '../Contact/ContactDetailStyle'
import { FontAwesome } from "@expo/vector-icons";
import colors from '../../config/colors';

interface props {
    text: string,
    itemKey: string
}
export default function ContactDetailRow({ text, itemKey }: props) {
    return (
        <View style={styles.colContainer}>
            <Text style={[styles.title, { fontSize: 20 }]}>{itemKey}</Text>
            <Text style={styles.textStyle}>{text}</Text>
        </View>
    )
}