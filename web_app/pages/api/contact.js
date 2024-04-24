import nodemailer from "modemailer";

export default async (req, res) => {
  const {name, email, message} = req.body

  const data = {
    name, email, message
  }
  const transporter = nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 465,
    secure: true,
    auth: {
      user: process.env.EMAIL_USERNAME,
      pass: process.env.EMAIL_PASSWORD,
    }
  });

  try {
    const mail = await transporter.sendEmail({
      from: user,
      to: "pedromoreirah3@gmail.com",
      replyTo: email,
      subject: `Contact form submission from ${name}`,
      html: `
      <p>Name ${name}</p>
      <p>Email ${email}</p>
      <p>Message ${message}</p>
      `
    })
  } catch (error) {
    console.log(error)
    res.status(500).json({message: "Could not send email. Your message was not sent."});
  }

  return res.status(200).json({message: "Success"})
}