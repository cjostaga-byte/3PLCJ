import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { AuthProvider } from './context/AuthContext';
import LoginTypeScreen from './screens/auth/LoginTypeScreen';
import EmployeeLoginScreen from './screens/auth/EmployeeLoginScreen';
import HRLoginScreen from './screens/auth/HRLoginScreen';
import AdminLoginScreen from './screens/auth/AdminLoginScreen';
import EmployeeDashboard from './screens/dashboards/EmployeeDashboard';

const Stack = createStackNavigator();

export default function App() {
  return (
    <AuthProvider>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="LoginType" component={LoginTypeScreen} />
          <Stack.Screen name="EmployeeLogin" component={EmployeeLoginScreen} />
          <Stack.Screen name="HRLogin" component={HRLoginScreen} />
          <Stack.Screen name="AdminLogin" component={AdminLoginScreen} />
          <Stack.Screen name="EmployeeDashboard" component={EmployeeDashboard} />
        </Stack.Navigator>
      </NavigationContainer>
    </AuthProvider>
  );
}
