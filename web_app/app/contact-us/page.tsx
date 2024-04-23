// pages/ContactUs.tsx
'use client';

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
      message: ''
    };
  }

  handleChange = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
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
      <div className="py-12 flex justify-center mt-6">
        <div className="px-4 sm:px-6 lg:px-8 w-full flex mt-6 justify-center ">
          <div className="bg-white rounded-lg shadow-lg w-1/2 p-10 my-6 flex flex-col justify-center">
            <div className="text-center mb-6">
              <h3 className="text-4xl sm:text-6xl font-bold"> Contact Us</h3>
            </div>
            <form
              onSubmit={this.handleSubmit}
              className="space-y-6 py-6 w-11/12 mx-auto"
            >
              <div>
                <label
                  htmlFor="name"
                  className="block text-sm font-medium text-gray-700"
                >
                  Name
                </label>
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
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700"
                >
                  Email
                </label>
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
              <div className=''>
                <label
                  htmlFor="message"
                  className="block text-sm font-medium text-gray-700"
                >
                  Message
                </label>
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
              <div className="flex justify-center ">
                <button
                  type="submit"
                  className=" flex justify-center py-2 px-4 border border-transparent bg-black text-white py-3 px-5 text-sm rounded-full shadow-sm text-sm font-medium text-white  "
                >
                  Send Message
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}
