<!--EDIT ITEM MODAL-->
		<div class="modal fade" id="edit-item" tabindex="-1" role="dialog" aria-labelledby="editLabel">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        		<h4 class="modal-title" id="editLabel"><strong>Edit Panel</strong></h4>
		      		</div>
			      	<div class="modal-body">
			      		<form data-toggle="validator" action="api/update.php" class="add-info" method="POST">
							<input type="hidden" name="id" class="edit-id"> <!--Different from Create Modal-->
							<div class="form-group">
								<label class="control-label" for="title">Invoice #</label>
								<input type="text" name="invoice_number" class="form-control" value="#" data-error="Please enter invoice # starting with # sign." required />
								<div class="help-block with-errors"></div>
							</div>
			      			<div class="form-group">
								<label class="control-label" for="title">Firm</label>
								<input type="text" name="firm" class="form-control" value="D" maxlength="1" data-error="Please enter title." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Office</label>
								<input type="text" name="office" class="form-control" value="UDN" maxlength="3" data-error="Please enter office." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Account</label>
								<input type="text" name="account" class="form-control" data-error="Please enter account." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Currency</label>
								<input type="text" name="currency" class="form-control" value="U1" maxlength="2" data-error="Please enter currency." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Off Office</label>
								<input type="text" name="off_office" class="form-control" value="UDN" maxlength="3" data-error="Please enter office." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Off Account</label>
								<input type="text" name="off_account" class="form-control" data-error="Please enter off account." required />
								<div class="help-block with-errors"></div>
							</div>

							<div class="form-group">
								<label class="control-label" for="title">Net Amount (-)</label>
								<input type="number" name="net_amount" class="form-control" max="0" value="-0.00" step=".01" data-error="Please enter a VALID net amount." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Description</label>
								<textarea name="description" class="form-control" data-error="Please enter description." required></textarea>
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Comment Code</label>
								<input type="text" name="comment_code" class="form-control" value="R" maxlength="1" data-error="Please enter comment code." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Adjust/Comments</label>
								<input type="text" name="comments" id="comments" class="form-control" style="margin-bottom: 20px;"/>
							</div>
							<div class="form-group">
								<button type="submit" id="submit" class="btn crud-submit-edit btn-success">Update</button>
							</div>
			      		</form>
					</div>
				</div>
			</div>
		</div>