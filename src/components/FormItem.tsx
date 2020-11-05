import React from 'react';
import { View, Text, TextInput, StyleSheet } from 'react-native';
import colors from '../../config/colors';

interface props {
    title: string;
    // onChange: () => void;
    // value: string;
    placeholder: string;
    style?: any;
}

export default function FormItem({title, placeholder, style, /*value, onChange*/}:props){
    return(
        <View style={styles.container}>
            <Text style={styles.title}>{title}</Text>
			<TextInput
                multiline
				style={[styles.inputStyle, style]}
                placeholder={placeholder}
                // value={value}
                // onChange={onChange}
			/>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex:1,
        width:'100%',
        alignItems:'center'
    },
    inputStyle: {
        width: '95%',
        height: 50,
        borderWidth: 1,
        marginHorizontal: 8,
        paddingHorizontal: 8,
        borderRadius: 10,
        borderColor: colors.borderColor
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
        width:'95%',
        marginVertical: 8
    },
})