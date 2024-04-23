// pages/ContactUs.tsx
'use client'

import React, { Component } from 'react';
import Link from 'next/link';
import Image from 'next/image';

interface State {
    name: string;
    email: string;
    message: string;
}

export default class ContactUs extends Component<{}, State> {
    constructor(props: {}) {
        super(props);
        this.state = {
            name: '',
            email: '',
            message: '',
        };
    }

    handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = event.target;
        this.setState({ [name]: value } as Pick<State, keyof State>);
    };

    handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log('Form Data:', this.state);
        // Add your form submission logic here
    };

    render() {
        return (
            <div className="bg-gray-100 py-12">
                <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="bg-white p-6 rounded-lg shadow-lg">
                        <h2 className="text-3xl font-bold text-center mb-10">Contact Us</h2>
                        <form onSubmit={this.handleSubmit} className="space-y-6">
                            <div>
                                <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name</label>
                                <input
                                    type="text"
                                    name="name"
                                    id="name"
                                    required
                                    className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                                    value={this.state.name}
                                    onChange={this.handleChange}
                                />
                            </div>
                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
                                <input
                                    type="email"
                                    name="email"
                                    id="email"
                                    required
                                    className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                                    value={this.state.email}
                                    onChange={this.handleChange}
                                />
                            </div>
                            <div>
                                <label htmlFor="message" className="block text-sm font-medium text-gray-700">Message</label>
                                <textarea
                                    name="message"
                                    id="message"
                                    rows={4}
                                    required
                                    className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                                    value={this.state.message}
                                    onChange={this.handleChange}
                                ></textarea>
                            </div>
                            <button
                                type="submit"
                                className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                            >
                                Send Message
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        );
    }
}
