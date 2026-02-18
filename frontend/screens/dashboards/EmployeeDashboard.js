import React, { useState, useEffect } from 'react';
import { View, Text, Button, TextInput, Image, StyleSheet } from 'react-native';
import { launchCamera } from 'react-native-image-picker';

const EmployeeDashboard = () => {
    const [employee, setEmployee] = useState({
        name: '',
        email: '',
        clockedIn: false,
        profileImage: null,
    });

    // Load employee data
    useEffect(() => {
        // Fetch employee data from API or local storage
        // For example purposes, we'll use static data
        setEmployee({
            name: 'John Doe',
            email: 'john.doe@example.com',
            clockedIn: false,
            profileImage: null,
        });
    }, []);

    const clockIn = () => {
        setEmployee(prev => ({ ...prev, clockedIn: true }));
        captureImage();
    };

    const clockOut = () => {
        setEmployee(prev => ({ ...prev, clockedIn: false }));
    };

    const captureImage = () => {
        launchCamera({}, (response) => {
            if (response.assets) {
                setEmployee(prev => ({ ...prev, profileImage: response.assets[0].uri }));
            }
        });
    };

    const updateProfile = (field, value) => {
        setEmployee(prev => ({ ...prev, [field]: value }));
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Employee Dashboard</Text>
            <TextInput
                placeholder="Name"
                value={employee.name}
                onChangeText={text => updateProfile('name', text)}
                style={styles.input}
            />
            <TextInput
                placeholder="Email"
                value={employee.email}
                onChangeText={text => updateProfile('email', text)}
                style={styles.input}
            />
            {employee.profileImage && <Image source={{ uri: employee.profileImage }} style={styles.image} />}  
            <Button title={employee.clockedIn ? 'Clock Out' : 'Clock In'} onPress={employee.clockedIn ? clockOut : clockIn} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
        justifyContent: 'center',
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 15,
        paddingHorizontal: 10,
    },
    image: {
        width: 100,
        height: 100,
        marginBottom: 15,
    },
});

export default EmployeeDashboard;