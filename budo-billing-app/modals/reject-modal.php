<!--SUBMIT SHEET MODAL-->
<div class="modal fade" id="reject-modal" tabindex="-1" role="dialog" aria-labelledby="createLabel"> 
	<div class="modal-dialog" role="document"> 
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        <h4 class="modal-title" id="editLabel"><strong>Reject Back</strong></h4>
			</div>
			<div class="modal-body"> 
				<div class="form-group">
					<form action="api/send_email.php" name="sendMail" method="POST" enctype="multipart/form-data">
						<strong><p>Select Recipients</p></strong>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="becky" name="recipients[]" value="becky.ali@budoholdings.com" disabled> Becky A.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang" name="recipients[]" value="boyang.dong@budoholdings.com"> Boyang D.
							</label>
						</div>	
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyang2" name="recipients[]" value="bdong.bobo@gmail.com"> Boyang Gmail
							</label>
						</div>					
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="corey" name="recipients[]" value="mike.caulfield@budoholdings.com" disabled> Mike C.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="mark" name="recipients[]" value="phil.pliskin@budoholdings.com" disabled> Phil P.
							</label>
						</div>
						<strong><p style="margin-top: 5px; margin-bottom: 5px;">Title</p></strong>
						<input type="text" name="mail_sub" class="form-control" value="REJECTED: Rebill Sheet Today"/>
						<strong><p style="margin-top: 10px; margin-bottom: 5px;">Message</p></strong>
						<textarea rows='3' name="mail_msg" class="form-control" data-error="Please say something..." required>Hi, please redo the spreadsheet..&#13;&#10;&#13;&#10;Thanks,</textarea>
						</br></br>
						<div class="form-group">
							<button type="submit" class="btn btn-danger send-email" name="send_email">Reject</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>

</div>