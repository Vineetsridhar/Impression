import React from 'react';
import { View, Text, TouchableOpacity, Linking } from 'react-native';
import styles from '../Contact/ContactDetailStyle'
import colors from '../../config/colors';

interface props {
    text: string,
    itemKey: string
}
export default function ContactDetailRow({ text, itemKey }: props):JSX.Element {
    const openEmail = () => {
        Linking.openURL('mailto:' + text)
    }
    return (
        <View style={styles.colContainer}>
            <Text style={[styles.title, { fontSize: 20 }]}>{itemKey}</Text>
            {itemKey == "Email" ? <TouchableOpacity onPress={openEmail}>
                <Text style={[styles.textStyle, { color: colors.main }]}>{text}</Text>
            </TouchableOpacity> : <Text style={styles.textStyle}>{text}</Text>
            }
        </View>
    )
}