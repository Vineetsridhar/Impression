import React from 'react';
import { Picker } from '@react-native-picker/picker';
import font from '../../config/font';
interface props {
    value: string,
    onChange: (term: React.ReactText, i: number) => void
}
export default function TypePicker({ value, onChange }: props) {
    return (
        <Picker
            selectedValue={value}
            style={{ width: "50%" }}
            onValueChange={onChange}>
            <Picker.Item label="Student" value="Student" />
            <Picker.Item label="Recruiter" value="Recruiter" />
        </Picker>
    )
}
